import subprocess

ps_script = r'''
$pp = New-Object -ComObject PowerPoint.Application
$pptxPath = "c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\Temas EB\Sesiones EB\Sesion 12\Sesion 12 - Flexibilidad externa, proteccion del empleo y dualidad laboral.pptx"
$pdfPath = "c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\Temas EB\Sesiones EB\Sesion 12\Sesion 12 - Flexibilidad externa, proteccion del empleo y dualidad laboral.pdf"
$pres = $pp.Presentations.Open($pptxPath, $true, $false, $false)
$pres.SaveAs($pdfPath, 32)
$pres.Close()
$pp.Quit()
Write-Host "PDF exportado con exito"
'''

with open(r"c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\Temas EB\Sesiones EB\Sesion 12\export_pdf.ps1", "w", encoding="utf-8") as f:
    f.write(ps_script)

res = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\Temas EB\Sesiones EB\Sesion 12\export_pdf.ps1"], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)

