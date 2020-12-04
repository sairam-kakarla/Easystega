
function previewEncodeImage() {
    var file = document.querySelector("#img").files[0];
    document.querySelector(".original").style.display="block";
    var reader=new FileReader();
    if(file){
        reader.readAsDataURL(file);
    }
    var image =new Image;
    image.src=URL.createObjectURL(file);
    console.log(image.src)
    document.querySelector(".original img").src=image.src}