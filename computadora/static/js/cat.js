// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla_categoria"; // id
var nombre_boton_eliminar = ".delete"; // Clase
var nombre_formulario_modal = "#frmEliminar"; //id
var nombre_ventana_modal = "#myModalC"; // id
// Fin de configuraciones


    $(document).on('ready',function(){
        $(nombre_boton_eliminar).on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idComponente').val(Pid);
            $('#modal_name').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        alert("Eliminado!");
                        var idComp = response.componente_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idComp).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }
                        
                    }else{
                        alert("Hubo un error al eliminar!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };

        $(nombre_formulario_modal).ajaxForm(options);
    });
