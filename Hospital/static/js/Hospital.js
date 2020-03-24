$(document).ready(function () {
    $('#dropdowndistrict').hide();
    $('#dropdownupazila').hide();
    $('#dropdownunion').hide();

    $('#DropDownDivision').change(function () {
        $('#DropDownDistrict').empty();
        $('#DropDownUpazila').empty();
        $('#DropDownUnion').empty();
        $('#dropdownupazila').hide();
        $('#dropdownunion').hide();
        $('#dropdowndistrict').show();
        var division_name = $("#DropDownDivision option:selected").val();

        $.getJSON('/SuperAdmin/GetDistrict/' + division_name, function (response) {
            console.log(response);
            $("#DropDownDistrict").append("<option> Select-Any-District </option>");
            $.each(response.Districts, function (i, value) {
                $("#DropDownDistrict").append("<option>" + value.District_name + "</option>");
            });
        });
    });

    $('#DropDownDistrict').change(function () {
        $('#DropDownUpazila').empty();
        $('#DropDownUnion').empty();
        $('#dropdownupazila').show();
        var district_name = $("#DropDownDistrict option:selected").val();

        $.getJSON('/SuperAdmin/GetUpazila/' + district_name, function (response) {
            console.log(response);
            $("#DropDownUpazila").append("<option> Select-Any-Upazila </option>");
            $.each(response.Upazilas, function (i, value) {
                $("#DropDownUpazila").append("<option>" + value.Upazila_name + "</option>");
            });
        });
    });

    $('#DropDownUpazila').change(function () {
        $('#DropDownUnion').empty();
        $('#dropdownunion').show();
        var upazila_name = $("#DropDownUpazila option:selected").val();

        $.getJSON('/SuperAdmin/GetUnion/' + upazila_name, function (response) {
            console.log(response);
            $("#DropDownUnion").append("<option> Select-Any-Union </option>");
            $.each(response.Unions, function (i, value) {
                $("#DropDownUnion").append("<option>" + value.Union_name + "</option>");
            });
        });
    });
});