$(document).ready(function () {
    $('#dropdowndivision').get(0).selectedIndex = 0;
    $('#dropdowndistrict').hide();
    $('#dropdownupazila').hide();

    $('#dropdowndivision').change(function () {
        $('#DropDownDistrict').empty();
        $('#DropDownUpazila').empty();
        $('#dropdownupazila').hide();
        $('#dropdowndistrict').show();
        var division_name = $("#dropdowndivision option:selected").val();

        $.getJSON('/SuperAdmin/GetDistrict/' + division_name, function (response) {
            console.log(response);
            $("#DropDownDistrict").append("<option> Select-Any-District </option>");
            $.each(response.Districts, function (i, value) {
                $("#DropDownDistrict").append("<option>" + value.District_name + "</option>");
            });
        });
    });

    $('#dropdowndistrict').change(function () {
        $('#DropDownUpazila').empty();
        $('#dropdownupazila').show();
        var district_name = $("#DropDownDistrict option:selected").val();

        $.getJSON('/SuperAdmin/GetUpazila/' + district_name, function (response) {
            console.log(response);
            $("#DropDownUpazila").append("<option> Select-Any-District </option>");
            $.each(response.Upazilas, function (i, value) {
                $("#DropDownUpazila").append("<option>" + value.Upazila_name + "</option>");
            });
        });
    });
});