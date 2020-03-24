$(document).ready(function () {

    $('#submit').click(function () {
        var district_name = $("#adddistrict").val();

        $.getJSON('/SuperAdmin/AllInformation/' + district_name, function (response) {
            console.log(response);
            $("#district").append("<option> Select-Any-District </option>");
            $.each(response.District, function (i, value) {
                $("#district").append("<option>" + value.AddDistrict + "</option>");
            });
        });
    });
})