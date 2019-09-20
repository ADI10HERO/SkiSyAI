document.getElementById("takePic").addEventListener("click",cameraTakePic);
document.getElementById("getPic").addEventListener("click",storageTakePic);
document.getElementById("upload-button").addEventListener("click",uploadPhoto);
//take pic from camera
function cameraTakePic() { 
     if (!navigator.camera) {
      alert("Camera API not supported", "Error");
      return;
      }
    var options =   {   quality: 100,
                        saveToPhotoAlbum : true,
                        allowEdit : true,
                        destinationType: Camera.DestinationType.FILE_URI,
                        sourceType: 1,      // 0:Photo Library, 1=Camera, 2=Saved Album
                        encodingType: 0     // 0=JPG 1=PNG
                     
                  };    
   navigator.camera.getPicture(onSuccess, onFail, options); 
}
//take pic from storage
function storageTakePic(){
    if (!navigator.camera) {
      alert("Camera API not supported", "Error");
      return;
      }
    var options = {
        quality: 100,
        allowEdit : true,
        sourceType : 2, // 0:Photo Library, 1=Camera, 2=Saved Album
        destinationType: Camera.DestinationType.FILE_URI,
        encodingType: 0     // 0=JPG 1=PNG
    };
    navigator.camera.getPicture(onSuccess, onFail, options);
}
//on success of getPicture()
function onSuccess(imageData) {
       document.getElementById('myimg').src = imageData;
       document.getElementById('upload-button').disabled = false;
}  
//on fail of getPicture()   
function onFail(message) { 
      alert('Failed because: ' + message); 
}
//upload image to server
function uploadPhoto() {
    var imageURI = document.getElementById('myimg').getAttribute("src");
    if(!imageURI) {
        alert("Please select an image first.");
    }
    var options = new FileUploadOptions();
    options.chunkedMode = false;
    options.headers = {
        Connection: "close"
    };
    options.fileKey = "file";
    options.fileName = imageURI.substr(imageURI.lastIndexOf('/')+1);
    options.mimeType = "image/jpg";
    var params = {};
    params.fname = document.getElementsByName("firstname").value;
    params.lname = document.getElementsByName("lastname").value;
    params.gender = document.getElementsByName("gender").value;
    params.age = document.getElementsByName("age").value;
    params.Historyofpresentillness = document.getElementsByName("Historyofpresentillness").value;
    params.history1 = document.getElementsByName("history1").value;
    params.history2 = document.getElementsByName("history2").value;
    params.history3 = document.getElementsByName("history3").value;
    params.history4 = document.getElementsByName("history4").value;
    params.symptom1 = document.getElementsByName("symptom1").value;
    params.symptom2 = document.getElementsByName("symptom2").value;
    params.symptom3 = document.getElementsByName("symptom3").value;
    params.symptom4 = document.getElementsByName("symptom4").value;
    params.symptom5 = document.getElementsByName("symptom5").value;
    params.Drugshistory = document.getElementsByName("Drugshistory").value;
    options.params = params;
    var ft = new FileTransfer();
    ft.upload(imageURI,encodeURI("http://34.93.236.101:7075/phonetest"), win, fail, options);
}
// on success of ft.upload()
function win(r) {
    window.localStorage.setItem("pred",r.response)
    window.location = "pred.html";
}
// on fail of ft.upload()
function fail(error) {
    alert("An error has occurred : Code = "+error.code);
}