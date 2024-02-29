let AWS = require("aws-sdk");
let polly = new AWS.Polly();
let s3 = new AWS.S3;
const uuidv1 = require('uuid/v1');

module.exports.speak = async(event, context, callback)=>{
  let data = JSON.parse(event.body);
  const pollyParams = {
    OutputFormat: "mp3",
    Text: data.text,
    VoiceId: data.voice
  };


  polly.synthesizeSpeech(pollyParams)
    .on("success", function (response) {
      let data= response.data;
      let audioStream = data.AudioStream;
      let key = uuidv1();
      let s3BucketName = 'polly-chat'

      //2.Saving the audio stream to S3
      let params = {
        Bucket: s3BucketName,
        key: key+ '.mp3',
        Body: audioStream
      };
      s3.putObject(params)
        .on("success" , function(response){
          console.log("S3 Put complete!");
        })
        .on("complete", function(){
          console.log("S3 Put Complete!");
          let s3Params = {
            Bucket: s3BucketName,
            key: key + '.mp3',
          };

          //getting a signed url for the saved mp3 file
          let url = s3.getSignedUrl("getObject", s3Params);

          //sending the result back to the user
          let result = {
            bucket: s3BucketName,
            key: key + '.mp3',
            url: url
          };
          callback(null, {
            statusCode: 200,
            headers: {
              "Access-Control-Allow-Origin" : "*"
            },
            body: JSON.stringify(result)
          }).send();
        })
        .on("error", function(err){
          callback(null, {
            statusCode: 500,
            Headers: {
              "Access-Control-Allow-Origin" : "*"
            },
            body: JSON.stringify(result)
          });
        })
        .send();
    }
    )

};