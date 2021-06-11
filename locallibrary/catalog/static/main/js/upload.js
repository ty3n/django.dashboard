function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

const csrftoken = getCookie('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("#FileSub").click(function() {
    var f_obj = $("#Upfile").get(0).files[0];                  
    console.log("object：",f_obj);
    console.log("object name:",f_obj.name);
    console.log("object size：",f_obj.size);

    var data = new FormData();                        
    data.append("file",f_obj)                                      

    $.ajax({
        url:'/files/'+f_obj.name,
        type:'PUT',
        data:f_obj,
        cache: false,                                               
        processData:false,                                          
        contentType:false,                                          
        success:function (arg) {
            alert("文件已經上傳成功，點擊確定刷新頁面");
            // console.log(arg);
            location.reload();
        }})
    });

// $(document).ready( function() {
const uploadForm = document.getElementById('upload-form')
console.log(uploadForm)
const input = document.getElementById('id_image')

const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const progressBox = document.getElementById('progress-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', ()=>{
	progressBox.classList.remove('not-visible')
	cancelBox.classList.remove('not-visible')
	const img_data = input.files[0]
	const fd = new FormData()
	fd.append('csrfmiddlewaretoken', csrf[0].value)
	fd.append('image', img_data)
	$.ajax({
		type:'POST',
		url:uploadForm.action,
		enctype: 'mutipart/form-data',
		data: fd,
		beforeSend: function(){

		},
		xhr:function(){
			const xhr = new window.XMLHttpRequest();
			xhr.upload.addEventListener('progress', e=>{
				if (e.lengthComputable) {
					const percent = e.loaded / e.total *100
					console.log(percent)
				}
			})
			return xhr
		},
		success: function(response){
			console.log(response)
		},
		error: function(error){
			console.log(error)
		},
        cache: false,                                               
        processData:false,                                          
        contentType:false,   
	})
})
// }