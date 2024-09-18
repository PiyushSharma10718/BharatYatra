console.log("payment working !");

$(document).ready(function () {
    $('.razorpay').click(function (e) {
        e.preventDefault();
        var name = $("[name = 'jsname']").val();
        var email = $("[name = 'jsemail']").val();
        var pack_name = $("[name = 'jspack_name']").val();
        var cat_name = $("[name = 'jscat_name']").val();
        var price = $("[name = 'jsprice']").val();

        // var phone = $("[name = 'phone']").val();

        // if(name == "" || email == "" || pack_name == "" || cat_name == "" || price == ""){
        //     swal("Alert", "Fill all the above Details !", "error");
        //     return false;
        // }
        // else{
            if(true){
            // yeh toh old hain !
            // old payment 1.0 !
            // var options = {
            //     "key": "rzp_test_4tIrxkRSCpEhLX",
            //     "amount": "50000",
            //     "currency": "INR",
            //     "name": "BharatYatra",
            //     "description": "Test Transaction",
            //     "image": "https://example.com/your_logo",
            //     // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            //     "handler": function (response){
            //         alert(response.razorpay_payment_id);
            //         // alert(response.razorpay_order_id);
            //         // alert(response.razorpay_signature)
            //     },
            //     "prefill": {
            //         "name": name,
            //         "email": gmail,
            //         "contact": phone,
            //     },
            //     "theme": {
            //         "color": "#3399cc"
            //     }
            // };
            // var rzp1 = new Razorpay(options);
            // rzp1.on('payment.failed', function (response){
            //         // alert(response.error.code);
            //         // alert(response.error.description);
            //         // alert(response.error.source);
            //         // alert(response.error.step);
            //         // alert(response.error.reason);
            //         // alert(response.error.metadata.order_id);
            //         alert(response.error.metadata.payment_id);
            // });
            //     rzp1.open();











            // new Payment 2.0
            var options = {
                "key": "rzp_test_d4DEwCLVLZ40Qn", // Enter the Key ID generated from the Dashboard
                "amount": "999900", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                "currency": "INR",
                "name": "BharatYatra", //your business name
                "description": "Test Transaction",
                "image": "https://example.com/your_logo",
                // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                "handler": function (response){
                    alert(response.razorpay_payment_id);
                    alert(response.razorpay_order_id);
                    alert(response.razorpay_signature)
                },
                "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                    "name": name, //your customer's name
                    "email": email,
                    "contact": "7041973300"  //Provide the customer's phone number for better conversion rates 
                },
                "theme": {
                    "color": "#3399cc"
                }
            };
            var rzp1 = new Razorpay(options);
            rzp1.on('payment.failed', function (response){
                    // alert(response.error.code);
                    // alert(response.error.description);
                    // alert(response.error.source);
                    // alert(response.error.step);
                    // alert(response.error.reason);
                    // alert(response.error.metadata.order_id);
                    alert(response.error.metadata.payment_id);
            });
            // document.getElementById('rzp-button1').onclick = function(e){
                rzp1.open();
        }
    });
});
