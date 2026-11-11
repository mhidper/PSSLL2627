
$pp = New-Object -ComObject PowerPoint.Application
$pptxPath = "c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\Temas EB\Sesiones EB\Sesion 12\Sesion 12 - Flexibilidad externa, proteccion del empleo y dualidad laboral.pptx"
$pdfPath = "c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\Temas EB\Sesiones EB\Sesion 12\Sesion 12 - Flexibilidad externa, proteccion del empleo y dualidad laboral.pdf"
$pres = $pp.Presentations.Open($pptxPath, $true, $false, $false)
$pres.SaveAs($pdfPath, 32)
$pres.Close()
$pp.Quit()
Write-Host "PDF exportado con exito"
