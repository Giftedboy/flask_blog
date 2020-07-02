window.onload = function(){
    var oLis = document.getElementsByClassName('for_js')
    var color = ['list-group-item-success', 'list-group-item-info', 'list-group-item-warning', 'list-group-item-danger']
    for(var i=0,j=0;i<oLis.length;i++,j++){
        if(j<=3){
            oLis[i].className += (' '+color[j]);
        }
        else{
            oLis[i].className += (' '+color[0]);
            j=0;
        }
    }
}