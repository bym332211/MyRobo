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
    $(function () { $('.popover-show').popover('show');});
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
            size : size
        });
    });
    $("#send").on("click",function(){
        var $content =$('#inputText').val();
        $('#inputText').val("");
        var $trSeq = "<tr><td></td><td><div style='float:right'><img src='static/img/hum.jpg' class='img-circle popover-show' data-container='body' data-placement='left' data-toggle='popover'  width='50' height='50'  data-content='" + $content + "'></div></td></tr>"
        var $table = $("#talk");
        $table.append($trSeq);
        $('.popover-show').popover('show');
        $.ajax({
            url: "/ajax",
            data: {
                type:"web",
                content:$content
            },
            dataType: "text",
            type: "POST",
            success: function(data) {
                var $trRep = "<tr><td><div><img src='static/img/robo.jpg' class='img-circle popover-show' data-container='body' data-placement='right' data-toggle='popover'  width='50' height='50'  data-content='" + data + "'></div></td></tr>"
                $table.append($trRep);
                $('.popover-show').popover('show');
            }
        });
    });
});

function deleteTr(aObject) {
        var flag = window.confirm("您确定要删除"+aObject.children(":first").text()+"名称的值吗？");
//      alert(flag);
         if(!flag){
          return false;
         } else {
          aObject.remove();
          return false;
         }
        return false;
      }
