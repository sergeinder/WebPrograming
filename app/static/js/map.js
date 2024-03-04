ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [55.777826, 37.623712],
            zoom: 12
        });
        var Placemark1 = new ymaps.Placemark([55.751594, 37.618051],{
            iconContent: 'Московский Кремль'
        },{preset: 'twirl#blueStretchyIcon'});
        myMap.geoObjects.add(Placemark1);
        var Placemark2 = new ymaps.Placemark([55.741449, 37.620882],{
            iconContent: 'Третьяковская галерея'
        },{preset: 'twirl#blueStretchyIcon'});
        myMap.geoObjects.add(Placemark2);
        var Placemark3 = new ymaps.Placemark([55.759637, 37.618803],{
            iconContent: 'Большой театр'
        },{preset: 'twirl#blueStretchyIcon'});
        myMap.geoObjects.add(Placemark3);
        var Placemark4 = new ymaps.Placemark([55.819708, 37.612590],{
            iconContent: 'Останкинская телебашня'
        },{preset: 'twirl#blueStretchyIcon'});
        myMap.geoObjects.add(Placemark4);
        var Placemark5 = new ymaps.Placemark([55.827983, 37.634973],{
            iconContent: 'ВДНХ'
        },{preset: 'twirl#blueStretchyIcon'});
        myMap.geoObjects.add(Placemark5);
        var Placemark6 = new ymaps.Placemark([55.749451, 37.542824],{
            iconContent: 'Москва-Сити'
        },{preset: 'twirl#blueStretchyIcon'});
        myMap.geoObjects.add(Placemark6);

        myMap.controls.add('zoomControl');
        myMap.controls.add('typeSelector');
    });