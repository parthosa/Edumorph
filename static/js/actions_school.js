jQuery(document).ready(function($){

  var detailFields=['Name','Address','City','State','Email','Contact','Principal','Concerned Authority'];
  //detailValue

  var paymentFields=[
    'Students Registered',
    'Students (Payment not recieved)',
    'Amount per student',
    'Other Charges',
    'Total Amount',
    'Amount Paid',
    'Amount Due'
  ];

  var statusFields=[
    'School Registered',
    'Enrollment sheet Uploaded',
    'Enrollment sheet Acknowledged',
    'Payment Accepted',
    'Roll numbers Generated',
    'Examination Conducted'
  ];

  var statusValue = [true,false,false,false,false,false];

  var rollNosAvail = true;
  //rollNosSheet

  var resultAvail = true;
  //resultSheet

  $('ul li:not(#home)').click(function() {
    $('.side,.head').slideUp();
    $('.main').removeClass('col-md-5');
    $('.main').addClass('col-md-10');
    $('.mainBox').empty();
    // $('.main').fadeIn();
    // loader();
    // setTimeout($('.mainBox').empty(),2000);
  });

  $('#home').click(function(){
    $('.main').removeClass('col-md-10');
    $('.main').addClass('col-md-5');
    $('.side,.head').slideDown();
    $('.mainBox').empty();
    $('.main .page-header h4').html('Basic Info <span style="float:right"><i class="material-icons edit">mode_edit</i></span>');
    for(i=0;i<detailFields.length-2;i++){
      var baseEle="<div class='row detail'><div class='col-xs-2 col-xs-offset-1'> <h5><strong>"+detailFields[i]+"</strong></h5> </div> <div class='col-xs-8 col-xs-offset-1 '> <h5 id="+detailFields[i].toLowerCase().replace(" ","_")+">value</h5> </div></div>";
      $('.mainBox').append(baseEle);
    }

  });


  $('#details').click(function(){
    $('.main .page-header h4').html('Info<span style="float:right"><i class="material-icons edit">mode_edit</i></span>');
    for(i=0;i<detailFields.length;i++){
      var baseEle="<div class='row detail'><div class='col-xs-2 col-xs-offset-1 col-md-offset-3'> <h5><strong>"+detailFields[i]+"</strong></h5> </div> <div class='col-xs-8 col-xs-offset-1 col-md-6'> <h5 id="+detailFields[i].toLowerCase().replace(" ","_")+">value</h5> </div></div>";
      $('.mainBox').append(baseEle);
    }
  });

  $('#enroll').click(function(){
    $('.main .page-header h4').html('Enrollment Sheet');
    $('.mainBox').append("<div class='row center-block' style='margin-top:1em'> <div class='col-xs-8 col-xs-offset-1 col-md-5 col-md-offset-0 text-center' > <a href='#' class='btn btn-sup btn-raised btn-sm'> <i class='material-icons'>file_download</i> <span>DOWNLOAD</span> </a> </div> <div class='col-xs-8 col-xs-offset-2 col-md-5 col-md-offset-1 text-center'><h6 class='text-danger'>*Fill the rows exactly in the format shown below. Do not modify the columns headers</h6></div> </div>");
    $('.mainBox').append("<div class='row center-block' style='margin-top:1em'> <div class='col-xs-8 col-xs-offset-1 col-md-5 col-md-offset-0 text-center' > <a href='#' class='btn btn-sup btn-raised btn-sm'> <i class='material-icons'>file_upload</i> <span>UPLOAD</span> </a> </div> <div class='col-xs-8 col-xs-offset-2 col-md-5 col-md-offset-1 text-center'><h6 class='text-danger'>*You can have multiple uploads before the deadline</h6></div> </div>");
    $('.mainBox').append("<div class='row center-block text-center' style='margin:6vh 0'><div class='col-xs-10 col-xs-offset-1 col-md-6 col-md-offset-3 text-center'><div class='page-header'></div><h3>Sample</h3></div><div class='col-xs-10 col-xs-offset-1 col-sm-6 col-sm-offset-3 text-center' style='margin-top:3vh'><img src='../img/table3.png' class='img-responsive'/></div></div>");
  });

  $('#payment').click(function(){
    $('.main .page-header h4').html('Payment');
    //call to get amount
    amount = 2500;
    var pay="<a href='https://www.instamojo.com/ankushedumorf/edumorph/' rel='im-checkout' data-behaviour='remote' data-style='flat' data-text='Checkout' data-token='35e9373a1fc1f62dfc9948bde7018bfe'></a> <script src='https://d2xwmjc4uy2hr5.cloudfront.net/im-embed/im-embed.min.js'></script>";
    $('.mainBox').append("<div class='row center-block' style='margin-top:1em;'><div class='col-xs-10 col-md-5 col-xs-offset-1 text-center'><div class='col-xs-7'><h5>Amount to be paid:</h5></div><div class='col-xs-4 col-xs-offset-1'> <h5>Rs "+amount+"</h5></div></div>  <div class='col-xs-8 col-md-3 col-xs-offset-2 text-center' >"+pay+"</div> </div>");
    $('.mainBox').append("<div class='row' style='margin-top:1em;'><div class='col-xs-12 text-left'><h6 class='text-info viewSummary' style='cursor:pointer'>*Click to view summary</h6></div></div>");
  });

  $('#status').click(function(){
    $('.main .page-header h4').html('Status');
    for(i=0;i<statusFields.length;i++){
      value = statusValue[i] ? "check" : "close" ;
      type = statusValue[i]? "success":"danger";
      var baseEle="<div class='row detail'><div class='col-xs-5 col-xs-offset-1 col-md-4 col-md-offset-2'> <h5><strong>"+statusFields[i]+"</strong></h5> </div> <div class='col-xs-2 col-xs-offset-1 col-md-3 col-md-offset-1 text-center'> <h5 id="+statusFields[i].toLowerCase().replace(" ","_")+"><i class='material-icons text-"+type+"' style='font-weight:bold'>"+value+"</i></h5> </div></div>";
      $('.mainBox').append(baseEle);
    }
  });

  $('#downloads').click(function(){
    $('.main .page-header h4').html('Downloads');
    if(rollNosAvail)
    content="<a href='#' class='btn btn-sup btn-raised btn-sm'> <i class='material-icons'>file_download</i> <span>DOWNLOAD</span> </a>";
    else
    content="<div class='alert alert-danger' style='color:white;margin-bottom:15px'><button type='button' class='close' >×</button>Please be patient till we finish the procedures </div>";
    $('.mainBox').append("<div class='row center-block' style='margin-top:1em;display: flex;justify-content: center;align-items: center;'><div class='col-xs-8 col-md-5 col-md-offset-1 text-center'><h5>Download the Roll Numbers sheet</h5></div>  <div class='col-xs-8 col-md-5 col-md-offset-0 text-center' > "+content+" </div> </div>");
  });

  $('#results').click(function(){
    $('.main .page-header h4').html('Results');
    if(resultAvail)
    content="<a href='#' class='btn btn-sup btn-raised btn-sm'> <i class='material-icons'>file_download</i> <span>DOWNLOAD</span> </a>";
    else
    content="<div class='alert alert-danger' style='color:white;margin-bottom:15px'><button type='button' class='close' >×</button>Please be patient our experts are still mining through best of our resourses </div>";
    $('.mainBox').append("<div class='row center-block' style='margin-top:1em;display: flex;justify-content: center;align-items: center;'><div class='col-xs-8 col-md-5 col-md-offset-1 text-center'><h5>Download Results</h5></div>  <div class='col-xs-8 col-md-5 col-md-offset-0 text-center' > "+content+" </div> </div>");
  });


  $(document).on('click','.edit',function(){
    $('.side,.head').fadeOut();
    $('.main').removeClass('col-md-5');
    $('.main').addClass('col-md-10');
    $('.mainBox').empty();
    $('.main .page-header h4').html('Edit Details');
    //call to get previous details
    $('.mainBox').append("<div class='row'> <div class='col-md-8 col-md-offset-2'> <form role='form' class='form-horizontal'> <fieldset> <div class='form-group'> <label class='control-label col-md-2' for='address'>Address</label> <div class='col-md-10'> <textarea  class='form-control' id='address' row='4' required /> </div> </div> <div class='form-group'> <label class='control-label col-md-2' for='email'> Email</label> <div class='col-md-10'> <input type='email' class='form-control' id='email' required> </div> </div> <div class='form-group'> <label class='control-label col-md-2' for='contact'> Contact</label> <div class='col-md-10'> <input type='text' class='form-control' id='contact' required> </div> </div> <div class='form-group'> <label class='control-label col-md-2' for='concerned_authority' >Concerned Authority</label> <div class='col-md-10'> <input type='text' class='form-control' id='concerned_authority'required > </div> </div> <div class='form-group'> <label class='control-label col-md-2' for='password'> Password</label> <div class='col-md-10'> <input type='password' class='form-control' id='password' required> </div> </div> <div class='form-group'> <label class='control-label col-md-2' for='confpassword'> Confirm Password</label> <div class='col-md-10'> <input type='password' class='form-control' id='confpassword' required> </div> </div> <div class='form-group'> <div class='col-md-8 col-md-offset-2 text-center'> <button type='submit' class='btn btn-info btn-raised'>Save Changes</button> </div> </div> </fieldset> </form> </div> </div>");
    $.material.init();
  });

  $(document).on('click','.viewSummary',function () {
    $('.side').slideDown();
    console.log('hi');
  });

  function loader() {
    spinner="<div class='spinnerWrap col-xs-10 col-xs-offset-1'><svg class='spinner' width='50px' height='50px' viewBox='0 0 66 66' xmlns='http://www.w3.org/2000/svg'><circle class='circle' fill='none' stroke-width='3' stroke-linecap='round' cx='33' cy='33' r='30'></circle></svg></div>";
    $('.mainBox').append(spinner);
  };
});
