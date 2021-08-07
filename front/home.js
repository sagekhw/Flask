const ButtonElement = document.querySelector('#Button');
const FileElement = document.querySelector('#File');

const getData = async () => {
    try{
        const formData = new FormData();

        for(let i = 0; i < FileElement.files.length; i++){
            formData.append("files", FileElement.files[i]);
	    //console.log(FileElement.files[i].name);
        }
        const company_data =  {
            "id":"",
            "pw":"test123",
            "name":"",
            
         };

        console.log(JSON.stringify(company_data));
        formData.append("jsonData",JSON.stringify(company_data));

        console.log(formData.get('jsonData'));

        const url = 'http://localhost:10005/file/fileUpload';
        const token = 'JWT token';
        console.log(token)

        const response = await axios({
                                    url: url
                                    ,method: 'post'
                                    ,data : formData
                                    ,headers: { 
                                        'Content-Type': 'multipart/form-data' 
                                        ,'Authorization': 'Bearer '+token 
                                    }
                                    });
        console.log(response)
    }
    catch (error){
        console.error(error);
    }
}

ButtonElement.addEventListener('click', getData);
