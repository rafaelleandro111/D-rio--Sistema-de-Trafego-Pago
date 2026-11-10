' Roda o rodar-diario.bat sem abrir janela (0 = escondido) e espera terminar.
Set fso = CreateObject("Scripting.FileSystemObject")
pasta = fso.GetParentFolderName(WScript.ScriptFullName)
CreateObject("WScript.Shell").Run """" & pasta & "\rodar-diario.bat""", 0, True
