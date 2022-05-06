$(document).ready(function () {

    let phase = $("#ci_pre_application_phase").val();

    if(phase == "welcome"){
        pre_application_ajax(phase);
    }

    $("#welcome_continue").click(function(e) {
    alert("dfgdfgdf")
        e.preventDefault();
        phase = "questionnaire";
        pre_application_ajax(phase);
    });

function pre_application_ajax(phase)
{
      const url = "/insurance/" + phase + "/"
      $.ajax({
          type : 'GET',
          url: url,
          data: {
              'phase': phase
          },
          beforeSend: function(){
              },
          success: function (data) {
                $("#ci_pre_application_phase").val(phase);
                $('.pre_application').html(data);
          },
              error: function () {
              alert('Oops!!!!! Something went wrong. Please try back after later');
          },
      });

}
});
