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
        $('.popover-show').popover('show');
        $('.popover-show').popover('disable');
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
//                    $(".alert").css({'visibility':'visible'});
                    $(".alert").show();
                    $('.popover-show').popover('togg');
                }else{
                    $(this).val("0");
//                    $(".alert").css({'visibility':'hidden'});
                    $(".alert").hide();
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
        $('.popover-show').popover('show');
        $('.popover-show').popover('disable');
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
                $('.popover-show').popover('show');
                $('.popover-show').popover('disable');
            }
        });
    });
});
function appendTr(tableObj, trStr) {
    tableObj.append(trStr);
    var cnt = 0;
    tableObj.find("tr").each(function () {
        cnt += 1;
        if (cnt > 8) {
            $trObj = tableObj.find("tbody").find("tr:first");
            deleteTr($trObj);
        }
    })
}
function deleteTr(trObj) {
//    trObj.find(".popover-show").each(function() {
//        $this = $(this);
//        $this.popover("destroy");
//    })
//    trObj.remove();
}
