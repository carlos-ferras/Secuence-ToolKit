; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define Package "Sequence-ToolKit"
#define MyAppVersion "2.3.5"
#define MyAppPublisher "University of Informatic Sciences"
#define Sequence-ToolKit "Sequence-ToolKit"
#define GenSec "GenSec"
#define GenRep "GenRep"
#define GenVis "GenVis"
#define STK-Assistant "STK-Assistant"
#define GenSecExe "GenSec.exe"
#define GenRepExe "GenRep.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{3161B261-B5E4-477A-B5B2-1AE358587A47}
AppName={#Package}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={pf}\{#Package}
DisableDirPage=yes
DefaultGroupName={#Package}
DisableProgramGroupPage=yes
LicenseFile=C:\Users\yanet\Desktop\dist\LICENSE
InfoBeforeFile=C:\Users\yanet\Desktop\dist\README.md
OutputDir=C:\Users\yanet\Desktop
OutputBaseFilename=Sequence-ToolKit
SetupIconFile=C:\Users\yanet\Desktop\dist\pixmaps\ico\app\package.ico
Compression=lzma
SolidCompression=yes 
ChangesAssociations=yes
AlwaysShowComponentsList=yes
ShowComponentSizes=yes
AppContact="c4rlos.ferra5@gmail.com"
AppCopyright=Copyright (C) 2015 Carlos Ferras.

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Components]
Name: "GenSec"; Description: "GenSec: Sequence Generator"; Types: full compact custom; Flags: checkablealone
Name: "GenRep"; Description: "GenRep: Report Generator"; Types: full compact custom; Flags: checkablealone


[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
;GENSEC
Source: "C:\Users\yanet\Desktop\dist\GenSec.exe"; DestDir: "{app}"; Components: GenSec
Source: "C:\Users\yanet\Desktop\dist\GenSec.exe.log"; DestDir: "{app}";Permissions: users-full; Components: GenSec  
;GENREP
Source: "C:\Users\yanet\Desktop\dist\GenRep.exe"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\GenRep.exe.log"; DestDir: "{app}";Permissions: users-full; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\mpl-data\*"; DestDir: "{app}\mpl-data\"; Components: GenRep; Flags:ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\yanet\Desktop\dist\tcl\*"; DestDir: "{app}\tcl\"; Components: GenRep; Flags:ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\yanet\Desktop\dist\_hashlib.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.multiarray_tests.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.random.mtrand.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\pyexpat.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib.ttconv.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\sip.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib._tri.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib.ft2font.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\GenRep.exe"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib.backends._backend_gdk.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.umath.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\bz2.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\python27.dll"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.operand_flag_tests.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\PyQt4.QtCore.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.fft.fftpack_lite.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\unicodedata.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\_elementtree.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.linalg._umath_linalg.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.umath_tests.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib._windowing.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.scalarmath.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib._delaunay.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\_socket.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core._dummy.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\PyQt4.QtGui.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib.backends._tkagg.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.test_rational.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.lib._compiled_base.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.struct_ufunc_test.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.linalg.lapack_lite.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\_tkinter.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib._png.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib._path.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib._image.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\select.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\tk85.dll"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib._cntr.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\_ctypes.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\libiomp5md.dll"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\tcl85.dll"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core._dotblas.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\QtGui4.dll"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\_ssl.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\numpy.core.multiarray.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib.backends._gtkagg.pyd"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\QtCore4.dll"; DestDir: "{app}"; Components: GenRep
Source: "C:\Users\yanet\Desktop\dist\matplotlib.backends._backend_agg.pyd"; DestDir: "{app}"; Components: GenRep
;BOTH
Source: "C:\Users\yanet\Desktop\dist\locale\*"; DestDir: "{app}\locale\";Components: GenRep GenSec; Flags:ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\yanet\Desktop\dist\theme\*"; DestDir: "{app}\theme\";Components: GenRep GenSec; Flags:ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\yanet\Desktop\dist\pixmaps\*"; DestDir: "{app}\pixmaps\";Components: GenRep GenSec; Flags:ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\yanet\Desktop\dist\_hashlib.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\pyexpat.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\sip.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\bz2.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\python27.dll"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\PyQt4.QtCore.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\unicodedata.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\_elementtree.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\_socket.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\PyQt4.QtGui.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\GenSec.exe"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\select.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\QtGui4.dll"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\_ssl.pyd"; DestDir: "{app}"; Components: GenSec GenRep
Source: "C:\Users\yanet\Desktop\dist\QtCore4.dll"; DestDir: "{app}"; Components: GenSec GenRep

[Registry]
;GENSEC
Root: HKCR; Subkey: ".slf"; ValueType: string; ValueName: ""; ValueData: "{#GenSec}"; Components: GenSec; Flags: uninsdeletevalue
Root: HKCR; Subkey: "{#GenSec}"; ValueType: string; ValueName: ""; ValueData: "{#GenSec}"; Components: GenSec; Flags: uninsdeletekey
Root: HKCR; Subkey: "{#GenSec}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\pixmaps\ico\file\slf.ico"; Components: GenSec
Root: HKCR; Subkey: "{#GenSec}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#GenSecExe}"" ""%1"""; Components: GenSec
;GENREP
Root: HKCR; Subkey: ".rlf"; ValueType: string; ValueName: ""; ValueData: "{#GenRep}"; Components: GenRep; Flags: uninsdeletevalue
Root: HKCR; Subkey: "{#GenRep}"; ValueType: string; ValueName: ""; ValueData: "{#GenRep}"; Components: GenRep; Flags: uninsdeletekey
Root: HKCR; Subkey: "{#GenRep}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\pixmaps\ico\file\rlf.ico"; Components: GenRep

[Icons]
;GENSEC
Name: "{group}\{#GenSec}"; Filename: "{app}\{#GenSecExe}"; WorkingDir: "{app}"; IconFilename: "{app}\pixmaps\ico\app\gensec.ico"; Components: GenSec 
Name: "{commondesktop}\{#GenSec}"; Filename: "{app}\{#GenSecExe}"; Tasks: desktopicon; Components: GenSec 
;GENREP
Name: "{group}\{#GenRep}"; Filename: "{app}\{#GenRepExe}"; WorkingDir: "{app}"; IconFilename: "{app}\pixmaps\ico\app\genrep.ico"; Components: GenRep
Name: "{commondesktop}\{#GenRep}"; Filename: "{app}\{#GenRepExe}"; Tasks: desktopicon; Components: GenRep
;UNINSTALL
Name: "{group}\{cm:UninstallProgram,{#Package}}"; Filename: "{uninstallexe}"







