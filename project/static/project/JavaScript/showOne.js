function addReportPro()
{
    let report =document.getElementById('report')
    if (report.style.display === "none") {
    report.style.display = "block";
    } else {
    report.style.display = "none";
    }
}
function addReportCom()
{
 let comment =document.getElementById('comment')
    if (comment.style.display === "none") {
    comment.style.display = "block";
    } else {
    comment.style.display = "none";
    }
    let id =document.getElementById('cId').name
    document.getElementById('comId').value= id

}