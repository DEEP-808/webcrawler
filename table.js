function populateTable(path)
{
    // requesting file data
    $.get(path,function(data)
    {
        var rows=data.split("\n");
        //getting all rows in the tesxt file
        for(var i=0;i<rows.length;i++)
        {
            var Rowpush = [];
            var rowData=rows[i].split(" ");
            //splitting row data to get individual data
            for(var j=0;j<rowData.length;j++)
            {
                if(rowData[j]=="")
                {
                }
                else{
                    Rowpush.push(rowData[j]);
                }
            }
            //creating row template
            var rowStruct= "<tr>";
            for(var k=0;k<Rowpush.length;k++)
            {
                //iterating through row and adding table data
                rowStruct+="<td>"+Rowpush[k]+"</td>";
            }
            rowStruct+="</tr>";
            //adding row template to the table
            $('#filetable').append(rowStruct);
        }
    });
}
//calling function
populateTable('./resf.txt');