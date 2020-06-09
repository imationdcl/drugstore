$( document ).ready(function() {

    urlBase = "http://localhost:5000/";

    $("#comunas").click(function() {
        var data_frm = new FormData();
        data_frm.append("reg_id", "7");

		$.ajax({
			//type: "POST",
			url: "https://midastest.minsal.cl/farmacias/maps/index.php/utilidades/maps_obtener_comunas_por_regiones",
            cache: false,
            contentType: false,
            processData: false,
            method: 'POST',
            type: 'POST', // For jQuery < 1.9
            data: data_frm
		}).done(function( result ) {
            $( "#comunas" ).html( result );            
		}).fail(function() {
			alert('Ha ocurrido un error, por favor intentelo nuevamente');
		});
    });

    $("#search-data").click(function(e) {
        e.preventDefault();

        var commune_id = $( "#comunas" ).val();
		var local_name 	= $( "#local_name" ).val().toUpperCase() ;

		$.ajax({
			type: "get",
			url: urlBase+"/drugstores",
			data: { local_nombre: local_name, comuna_id: commune_id}
		}).done(function( result ) {
            $( "#content-drugstore" ).html("");
            data = result.data
            data.forEach(element => {
                html = "<tr>";
                html += "<td>"+element.local_nombre+"</td>"; 
                html += "<td>"+element.local_direccion+"</td>"; 
                html += "<td>"+element.local_telefono+"</td>"; 
                html += "<td>"+element.local_lat+"</td>"; 
                html += "<td>"+element.local_lng+"</td>"; 
                html += "</td>"; 

                $( "#content-drugstore" ).append( html );
                html = '';
            });
		}).fail(function() {
			alert('Ha ocurrido un error, por favor intentelo nuevamente');
		});
    });

    function getAllDrugstores(){
        console.log("llamada")
        $.ajax({
            type: "get",
            url: urlBase+"/drugstores",
            data: {}
        }).done(function( result ) {
            $( "#content-drugstore" ).html("");
            data = result.data
            data.forEach(element => {
                html = "<tr>";
                html += "<td>"+element.local_nombre+"</td>"; 
                html += "<td>"+element.local_direccion+"</td>"; 
                html += "<td>"+element.local_telefono+"</td>"; 
                html += "<td>"+element.local_lat+"</td>"; 
                html += "<td>"+element.local_lng+"</td>"; 
                html += "</td>"; 

                $( "#content-drugstore" ).append( html );
                html = '';
            });
        }).fail(function() {
            alert('Ha ocurrido un error, por favor intentelo nuevamente');
        });
    }

    $.get(urlBase+"/drugstores", function(result) {
        $( "#content-drugstore" ).html("");
        data = result.data
        data.forEach(element => {
            html = "<tr>";
            html += "<td>"+element.local_nombre+"</td>"; 
            html += "<td>"+element.local_direccion+"</td>"; 
            html += "<td>"+element.local_telefono+"</td>"; 
            html += "<td>"+element.local_lat+"</td>"; 
            html += "<td>"+element.local_lng+"</td>"; 
            html += "</td>"; 

            $( "#content-drugstore" ).append( html );
            html = '';
        });
    });
});
