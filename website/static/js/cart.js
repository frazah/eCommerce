var updateButtons = document.getElementsByClassName('update-cart')

for(i=0; i< updateButtons.length; i++)
{

    updateButtons[i].addEventListener('click',function(){
    var productId= this.dataset.product
    var action = this.dataset.action
    updateUserOrder(productId,action)
    })
}


function updateUserOrder(productId,action){
var url = ('update_item/')
 console.log('a')
fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X.CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
        //console.log(JSON.stringify({'productId':productId, 'action':action}))
      }) //console.log(response)
    .then((response) => { console.log('Response:', response); return response.json() })
    .then((data) => { location.reload() })
    }
