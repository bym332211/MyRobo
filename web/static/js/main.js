/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under the MIT license
 */
//$(function() {
//    $( ".ui-widget-content" ).draggable();
//});

$(document).ready(function(){
    $(".draggable").each(function() {
        $this = $(this);
        $this.draggable();
    });
    $(function () {
        showpopover();
    });
    $(".switch").each(function() {
        $this = $(this);
        var onColor = $this.attr("data-on");
        var offColor = $this.attr("data-off");
        var onText = $this.attr("onText");
        var offText = $this.attr("offText");
        var labelText = $this.attr("labelText");
        var size = $this.attr("size");

        var $switch_input = $(" :only-child", $this);
        $switch_input.bootstrapSwitch({
            onColor : onColor,
            offColor : offColor,
            onText : onText,
            offText : offText,
            labelText : labelText,
            size : size,
            onSwitchChange:function(event,state){
                if(state==true){
                    $(this).val("1");
                    $(this).attr("checked", true);
//                    $(".alert").css({'visibility':'visible'});
                    $(".alert").show();
                    refreshpopover();
                    asrListening();
                }else{
                    $(this).val("0");
                    $(this).attr("checked", false);
//                    $(".alert").css({'visibility':'hidden'});
                    $(".alert").hide();
                    refreshpopover();
                }
            }
        });
    });
    $("#send").on("click",function(){
        var $content =$('#inputText').val();
        var $asr =$('#my-checkbox').val();
        var $playMode
        if ($asr == "1") {
            $playMode = "server"
        } else {
            $playMode = "web"
        }
        $('#inputText').val("");
        var $trSeq = "<tr><td></td><td><div style='float:right'><img src='static/img/hum.jpg' class='img-circle popover-show' data-container='body' data-placement='left' data-toggle='popover'  width='50' height='50'  data-content='" + $content + "'></div></td></tr>"
        var $table = $("#talk");
        appendTr($table, $trSeq)
        showpopover();
        $.ajax({
            url: "/ajax",
            data: {
                type:"web",
                playMode:$playMode,
                content:$content
            },
            dataType: "text",
            type: "POST",
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                var $trRep = "<tr><td><div><img src='static/img/robo.jpg' class='img-circle popover-show' data-container='body' data-placement='right' data-toggle='popover'  width='50' height='50'  data-content='" + obj.res + "'></div></td></tr>"
                if ($playMode == "web") {
                    var player = $("#player")[0]
                    player.src=obj.mp3;
                    player.play();
                }
                appendTr($table, $trRep)
                showpopover();
            }
        });
    });
});

function asrListening() {

    setInterval(function(){
//            host = window.location.host
//            $.post("http://"+host+"/index.php/Article/cpMes/value/1");
    var $table = $("#talk");
    $.ajax({
        url: "/ajax",
        data: {
            type:"asr",
            playMode:"server"
        },
        dataType: "text",
        type: "POST",
        success: function(data) {
                var obj = jQuery.parseJSON(data);
                var $trSeq = "<tr><td></td><td><div style='float:right'><img src='static/img/hum.jpg' class='img-circle popover-show' data-container='body' data-placement='left' data-toggle='popover'  width='50' height='50'  data-content='" + obj.content + "'></div></td></tr>"
                var $trRep = "<tr><td><div><img src='static/img/robo.jpg' class='img-circle popover-show' data-container='body' data-placement='right' data-toggle='popover'  width='50' height='50'  data-content='" + obj.res + "'></div></td></tr>"
//                if ($playMode == "web") {
//                    var player = $("#player")[0]
//                    player.src=obj.mp3;
//                    player.play();
//                }
                appendTr($table, $trSeq)
                appendTr($table, $trRep)
                showpopover();
            }
    });

    },5000);
}
function appendTr(tableObj, trStr) {
    tableObj.append(trStr);
    cnt = 0;
    tableObj.find("tbody").find("tr").each(function() {
        cnt = cnt + 1;
    });
    if (cnt > 6) {
        deleteTr(tableObj.find("tbody").find("tr:first"))
    }
    showpopover();
}
function deleteTr(trObj) {
    trObj.find(".popover-show:first").popover('destroy');
    trObj.remove();
}

function showpopover(){
    $('.popover-show').popover('show');
//    $('.popover-show').popover('disable');
}

function hidepopover(){
    $('.popover-show').popover('hide');
//    $('.popover-show').popover('disable');
}

function refreshpopover() {
//    hidepopover();
    showpopover();
}