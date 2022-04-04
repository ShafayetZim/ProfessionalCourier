var send_data = {}
//updates the total price by multiplying 'price per item' and 'quantity'
        $(document).on('change', '.setprice', function(e){
            e.preventDefault();
            //gets the values
            var element = $(this);

            var quantity = element('.form-row').find('.quantity').val();
            var perprice = element('.form-row').find('.price').val();

            //calculates the total
            var tprice = quantity * perprice;
            //sets it to field
            element('.form-row').find('.total').val(tprice);

           setTotalQtyAndAmount();


            //Set Total
             //$("#sales_total_amount").val(total_price);
             //$("#sales_total_qty").val(total_qty);
            return false;
        });