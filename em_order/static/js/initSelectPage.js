    var allFood = {{ allFood|safe }};
    $('#selectPage1').selectPage({
    showField : 'fName',
    keyField : 'fName',
    data : allFood,
    multiple : true
});
    $('#selectPage2').selectPage({
    showField : 'fName',
    keyField : 'fName',
    data : allFood,
    multiple : true
});
    $('#selectPage3').selectPage({
    showField : 'fName',
    keyField : 'fName',
    data : allFood,
    multiple : true
});
    laydate.render({
      elem: '#menuDate',
    });

