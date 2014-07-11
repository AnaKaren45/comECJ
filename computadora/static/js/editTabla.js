var btnEdit=false;
var btnSave=false;
var nRow;
var oTable = $('#tabla-1').dataTable();

$(document).ready(function()
{
	$('#tabla-1 tbody').on( 'click', 'tr', function (e) 
	{
	if(btnEdit)
	{
		nRow=$(this)[0];
		editRow(oTable, nRow);
		btnEdit=false;
	}
	if(btnSave)
	{
		nRow=$(this)[0];
		saveRow(oTable, nRow);
		btnSave=false;
	}
	});
});
function editRow(oTable, nRow)
{
	var aData = oTable.fnGetData(nRow);
	var jqTds = $('>td', nRow);
	jqTds[4].innerHTML ='<div class="input-control text"><input type="text" class="bg-darkRed fg-white" value="'+aData[4]+'"/><button class="btn-clear"></button></div>';
	jqTds[5].innerHTML = '<a class="button small danger" onClick="save()">guardar</a>';
}
		
function saveRow ( oTable, nRow )
{
	var jqInputs = $('input', nRow);
	var valor=jqInputs[0].value;
	if (/^([0-9])*[.]?[0-9]*$/.test(valor))
	{
		oTable.fnUpdate( valor, nRow, 4, false );//valor-columna
		var jqTds = $('>td', nRow);
		jqTds[5].innerHTML = '<a class="button small primary" onClick="edit()">editar</a>';
	}
	else
	{
			alert("Error");
	}
}
function save()
{
	btnSave=true;
}
function edit()
{
	
	btnEdit=true;
}