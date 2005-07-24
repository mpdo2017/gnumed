; Script generated by the HM NIS Edit Script Wizard.

; Find a way to automagically detect python location
; hardcode path and version for now - 2.3(23), 2.4(24)
!define PYTHON_VERSION "23"
!define PYTHON_PATH "C:\Python${PYTHON_VERSION}"

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "GNUmed-client"
!define PRODUCT_VERSION "0.1"
!define PRODUCT_PUBLISHER "GNUmed Systemhaus"
!define PRODUCT_WEB_SITE "http://www.gnumed.de"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "gnumed\GnuPublicLicense.txt"
; Components page
!insertmacro MUI_PAGE_COMPONENTS
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$PROGRAMFILES\GNUmed-client"
ShowInstDetails show
ShowUnInstDetails show

Section "Programmdateien" SEC01
  SetOverwrite try
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed"
  File "gnumed\gnumed\client\__init__.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\business"
  File "gnumed\gnumed\client\business\gmAllergy.py"
  File "gnumed\gnumed\client\business\gmClinicalRecord.py"
  File "gnumed\gnumed\client\business\gmClinItem.py"
  File "gnumed\gnumed\client\business\gmClinNarrative.py"
  File "gnumed\gnumed\client\business\gmDemographicRecord.py"
  File "gnumed\gnumed\client\business\gmEMRStructItems.py"
  File "gnumed\gnumed\client\business\gmForms.py"
  File "gnumed\gnumed\client\business\gmKVK.py"
  File "gnumed\gnumed\client\business\gmMedDoc.py"
  File "gnumed\gnumed\client\business\gmOrganization.py"
  File "gnumed\gnumed\client\business\gmPathLab.py"
  File "gnumed\gnumed\client\business\gmPerson.py"
  File "gnumed\gnumed\client\business\gmSOAPimporter.py"
  File "gnumed\gnumed\client\business\gmVaccination.py"
  File "gnumed\gnumed\client\business\gmXdtMappings.py"
  File "gnumed\gnumed\client\business\gmXdtObjects.py"
  File "gnumed\gnumed\client\business\gmXmlDocDesc.py"
  File "gnumed\gnumed\client\business\README"
  File "gnumed\gnumed\client\business\__init__.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\exporters"
  File "gnumed\gnumed\client\exporters\gmPatientExporter.py"
  File "gnumed\gnumed\client\exporters\__init__.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\importers"
  File "gnumed\gnumed\client\importers\gmLDTimporter.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon"
  File "gnumed\gnumed\client\pycommon\gmBackendListener.py"
  File "gnumed\gnumed\client\pycommon\gmBorg.py"
  File "gnumed\gnumed\client\pycommon\gmBusinessDBObject.py"
  File "gnumed\gnumed\client\pycommon\gmCfg.py"
  File "gnumed\gnumed\client\pycommon\gmCLI.py"
  File "gnumed\gnumed\client\pycommon\gmConfigCommon.py"
  File "gnumed\gnumed\client\pycommon\gmdbf.py"
  File "gnumed\gnumed\client\pycommon\gmDispatcher.py"
  File "gnumed\gnumed\client\pycommon\gmDrugObject.py"
  File "gnumed\gnumed\client\pycommon\gmDrugView.py"
  File "gnumed\gnumed\client\pycommon\gmExceptions.py"
  File "gnumed\gnumed\client\pycommon\gmGuiBroker.py"
  File "gnumed\gnumed\client\pycommon\gmI18N.py"
  File "gnumed\gnumed\client\pycommon\gmLog.py"
  File "gnumed\gnumed\client\pycommon\gmLoginInfo.py"
  File "gnumed\gnumed\client\pycommon\gmMatchProvider.py"
  File "gnumed\gnumed\client\pycommon\gmMimeLib.py"
  File "gnumed\gnumed\client\pycommon\gmMimeMagic.py"
  File "gnumed\gnumed\client\pycommon\gmNull.py"
  File "gnumed\gnumed\client\pycommon\gmPG.py"
  File "gnumed\gnumed\client\pycommon\gmPsql.py"
  File "gnumed\gnumed\client\pycommon\gmPyCompat.py"
  File "gnumed\gnumed\client\pycommon\gmSchemaRevisionCheck.py"
  File "gnumed\gnumed\client\pycommon\gmScriptingListener.py"
  File "gnumed\gnumed\client\pycommon\gmSerialTools.py"
  File "gnumed\gnumed\client\pycommon\gmSignals.py"
  File "gnumed\gnumed\client\pycommon\gmWhoAmI.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools"
  File "gnumed\gnumed\client\pycommon\tools\debugging_off.py"
  File "gnumed\gnumed\client\pycommon\tools\set-conf_opt.py"
  File "gnumed\gnumed\client\pycommon\tools\show_img.py"
  File "gnumed\gnumed\client\pycommon\tools\stripdos.py"
  File "gnumed\gnumed\client\pycommon\tools\transferDBset.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon"
  File "gnumed\gnumed\client\pycommon\__init__.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed"
  File "gnumed\gnumed\client\sitecustomize.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython"
  File "gnumed\gnumed\client\wxpython\gmAbout.py"
  File "gnumed\gnumed\client\wxpython\gmAllergyWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmAppoint.py"
  File "gnumed\gnumed\client\wxpython\gmBMIWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmCharacterValidator.py"
  File "gnumed\gnumed\client\wxpython\gmCryptoText.py"
  File "gnumed\gnumed\client\wxpython\gmDateTimeInput.py"
  File "gnumed\gnumed\client\wxpython\gmDemographicsWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmEditArea.py"
  File "gnumed\gnumed\client\wxpython\gmEMRBrowser.py"
  File "gnumed\gnumed\client\wxpython\gmEMRStructWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmEMRTextDump.py"
  File "gnumed\gnumed\client\wxpython\gmFormPrinter.py"
  File "gnumed\gnumed\client\wxpython\gmGP_ActiveProblems.py"
  File "gnumed\gnumed\client\wxpython\gmGP_FamilyHistorySummary.py"
  File "gnumed\gnumed\client\wxpython\gmGP_HabitsRiskFactors.py"
  File "gnumed\gnumed\client\wxpython\gmGP_Inbox.py"
  File "gnumed\gnumed\client\wxpython\gmGP_PatientPicture.py"
  File "gnumed\gnumed\client\wxpython\gmGP_SocialHistory.py"
  File "gnumed\gnumed\client\wxpython\gmGuiHelpers.py"
  File "gnumed\gnumed\client\wxpython\gmGuiMain.py"
  File "gnumed\gnumed\client\wxpython\gmHorstSpace.py"
  File "gnumed\gnumed\client\wxpython\gmLabWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmListCtrlMapper.py"
  File "gnumed\gnumed\client\wxpython\gmLogin.py"
  File "gnumed\gnumed\client\wxpython\gmLoginDialog.py"
  File "gnumed\gnumed\client\wxpython\gmMacro.py"
  File "gnumed\gnumed\client\wxpython\gmMedDocWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmMultiColumnList.py"
  File "gnumed\gnumed\client\wxpython\gmMultiSash.py"
  File "gnumed\gnumed\client\wxpython\gmPatientHolder.py"
  File "gnumed\gnumed\client\wxpython\gmPatPicWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmPatSearchWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmPhraseWheel.py"
  File "gnumed\gnumed\client\wxpython\gmPlugin.py"
  File "gnumed\gnumed\client\wxpython\gmPlugin_Patient.py"
  File "gnumed\gnumed\client\wxpython\gmPregWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmRegetMixin.py"
  File "gnumed\gnumed\client\wxpython\gmResizingWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmRichardSpace.py"
  File "gnumed\gnumed\client\wxpython\gmSelectPerson.py"
  File "gnumed\gnumed\client\wxpython\gmShadow.py"
  File "gnumed\gnumed\client\wxpython\gmSOAPWidgets.py"
  File "gnumed\gnumed\client\wxpython\gmSQLListControl.py"
  File "gnumed\gnumed\client\wxpython\gmSQLSimpleSearch.py"
  File "gnumed\gnumed\client\wxpython\gmTalkback.py"
  File "gnumed\gnumed\client\wxpython\gmTerryGuiParts.py"
  File "gnumed\gnumed\client\wxpython\gmTimer.py"
  File "gnumed\gnumed\client\wxpython\gmTopPanel.py"
  File "gnumed\gnumed\client\wxpython\gmVaccWidgets.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui"
  File "gnumed\gnumed\client\wxpython\gui\gmAllergiesPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmClinicalWindowManager.py"
  File "gnumed\gnumed\client\wxpython\gui\gmConfigRegistry.py"
  File "gnumed\gnumed\client\wxpython\gui\gmContacts.py"
  File "gnumed\gnumed\client\wxpython\gui\gmDemographicsEditor.py"
  File "gnumed\gnumed\client\wxpython\gui\gmDrugDisplay.py"
  File "gnumed\gnumed\client\wxpython\gui\gmEMRBrowserPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmEMRJournalPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmEMRTextDumpPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmGuidelines.py"
  File "gnumed\gnumed\client\wxpython\gui\gmLabJournal.py"
  File "gnumed\gnumed\client\wxpython\gui\gmManual.py"
  File "gnumed\gnumed\client\wxpython\gui\gmMultiSashedProgressNoteInputPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmNotebookedPatientEditionPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmNotebookedProgressNoteInputPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmOffice.py"
  File "gnumed\gnumed\client\wxpython\gui\gmplNbSchedule.py"
  File "gnumed\gnumed\client\wxpython\gui\gmPython.py"
  File "gnumed\gnumed\client\wxpython\gui\gmRequest.py"
  File "gnumed\gnumed\client\wxpython\gui\gmShowLab.py"
  File "gnumed\gnumed\client\wxpython\gui\gmShowMedDocs.py"
  File "gnumed\gnumed\client\wxpython\gui\gmSnellen.py"
  File "gnumed\gnumed\client\wxpython\gui\gmSQL.py"
  File "gnumed\gnumed\client\wxpython\gui\gmStikoBrowser.py"
  File "gnumed\gnumed\client\wxpython\gui\gmVaccinationsPlugin.py"
  File "gnumed\gnumed\client\wxpython\gui\gmXdtViewer.py"
  File "gnumed\gnumed\client\wxpython\gui\__init__.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython"
  File "gnumed\gnumed\client\wxpython\images.py"
  File "gnumed\gnumed\client\wxpython\images_Archive_plugin.py"
  File "gnumed\gnumed\client\wxpython\images_Archive_plugin1.py"
  File "gnumed\gnumed\client\wxpython\images_contacts_toolbar16_16.py"
  File "gnumed\gnumed\client\wxpython\images_for_gnumed_browser16_16.py"
  File "gnumed\gnumed\client\wxpython\images_gnumedGP.py"
  File "gnumed\gnumed\client\wxpython\images_gnumedGP_notebook.py"
  File "gnumed\gnumed\client\wxpython\images_gnuMedGP_Toolbar.py"
  File "gnumed\gnumed\client\wxpython\images_patient_demographics.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient"
  File "gnumed\gnumed\client\wxpython\patient\gmCrypto.py"
  File "gnumed\gnumed\client\wxpython\patient\gmDemographics.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_Allergies.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_AnteNatal_3.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_ClinicalSummary.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_FamilyHistory.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_Immunisation.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_Measurements.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_PastHistory.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_PatientPlugin.py.template"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_Prescriptions.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_Recalls.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_Referrals.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_Requests.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_ScratchPadRecalls.py"
  File "gnumed\gnumed\client\wxpython\patient\gmGP_TabbedLists.py"
  File "gnumed\gnumed\client\wxpython\patient\__init__.py"
  SetOutPath "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython"
  File "gnumed\gnumed\client\wxpython\__init__.py"
  SetOutPath "$INSTDIR\bin"
  File "gnumed\gnumed\client\wxpython\gnumed.py"
  SetOutPath "$INSTDIR"
  File "gnumed\gnumed\client\__init__.py"
  File "gnumed\gnumed\client\gm-0_1.conf"
  SetOverwrite ifnewer
  File "gnumed\gnumed\client\gnumed.bat"
  SetOutPath "$INSTDIR\bitmaps"
  File "gnumed\gnumed\client\wxpython\__init__.py"
  File "gnumed\gnumed\client\bitmaps\any_body2.png"
  File "gnumed\gnumed\client\bitmaps\binoculars_form.png"
  File "gnumed\gnumed\client\bitmaps\bmi_calculator.png"
  File "gnumed\gnumed\client\bitmaps\default.png"
  File "gnumed\gnumed\client\bitmaps\empty-face-in-bust.png"
  File "gnumed\gnumed\client\bitmaps\gnumedlogo.png"
  File "gnumed\gnumed\client\bitmaps\oneperson.png"
  File "gnumed\gnumed\client\bitmaps\padlock_closed.png"
  File "gnumed\gnumed\client\bitmaps\preg_calculator.png"
  File "gnumed\gnumed\client\bitmaps\save.png"
  File "gnumed\gnumed\client\bitmaps\serpent.png"
  CreateDirectory "$SMPROGRAMS\GNUmed"
  CreateShortCut "$SMPROGRAMS\GNUmed\GNUmed.lnk" "$INSTDIR\gnumed.bat"
SectionEnd

;Section "Sprachdateien" SEC02
;  SetOutPath "$INSTDIR\locale\de\LC_MESSAGES"
;  SetOverwrite try
;  File "gnumed\gnumed\client\locale\de\LC_MESSAGES\gnumed.mo"
;  SetOutPath "$INSTDIR\locale\de_DE\LC_MESSAGES"
;  File "gnumed\gnumed\client\locale\de_DE\LC_MESSAGES\gnumed.mo"
;  SetOutPath "$INSTDIR\locale\es\LC_MESSAGES"
;  File "gnumed\gnumed\client\locale\es\LC_MESSAGES\gnumed.mo"
;  SetOutPath "$INSTDIR\locale\es_ES\LC_MESSAGES"
;  File "gnumed\gnumed\client\locale\es_ES\LC_MESSAGES\gnumed.mo"
;  SetOutPath "$INSTDIR\locale\fr\LC_MESSAGES"
;  File "gnumed\gnumed\client\locale\fr\LC_MESSAGES\gnumed.mo"
;  SetOutPath "$INSTDIR\locale\fr_FR\LC_MESSAGES"
;  File "gnumed\gnumed\client\locale\fr_FR\LC_MESSAGES\gnumed.mo"
;SectionEnd

Section "Dokumentation" SEC03
  SetOutPath "$INSTDIR\doc\medical_knowledge\de\STIKO"
  File "gnumed\gnumed\client\doc\medical_knowledge\de\STIKO\STI_NEU.htm"
  SetOutPath "$INSTDIR\doc\user-manual"
;  File "gnumed\gnumed\client\doc\client\user-manual\*.html"
SectionEnd

Section -AdditionalIcons
  SetOutPath $INSTDIR
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateDirectory "$SMPROGRAMS\GNUmed"
  CreateShortCut "$SMPROGRAMS\GNUmed\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\GNUmed\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

; Section descriptions
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC01} "all files needed for running GNUmed"
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC02} "files for non-English user interface"
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC03} "user manual"
!insertmacro MUI_FUNCTION_DESCRIPTION_END


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) wurde erfolgreich deinstalliert."
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "M�chten Sie $(^Name) und alle seinen Komponenten deinstallieren?" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\doc\medical_knowledge\de\STIKO\STI_NEU.htm"
  Delete "$INSTDIR\doc\user-manual\*.html"
  Delete "$INSTDIR\locale\fr_FR\LC_MESSAGES\gnumed.mo"
  Delete "$INSTDIR\locale\fr\LC_MESSAGES\gnumed.mo"
  Delete "$INSTDIR\locale\es_ES\LC_MESSAGES\gnumed.mo"
  Delete "$INSTDIR\locale\es\LC_MESSAGES\gnumed.mo"
  Delete "$INSTDIR\locale\de_DE\LC_MESSAGES\gnumed.mo"
  Delete "$INSTDIR\locale\de\LC_MESSAGES\gnumed.mo"
  Delete "$INSTDIR\gnumed.bat"
  Delete "$INSTDIR\__init__.py"
  Delete "$INSTDIR\*.*"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\__init__.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\__init__.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_TabbedLists.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_ScratchPadRecalls.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_Requests.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_Referrals.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_Recalls.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_Prescriptions.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_PatientPlugin.py.template"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_PastHistory.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_Measurements.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_Immunisation.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_FamilyHistory.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_ClinicalSummary.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_AnteNatal_3.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmGP_Allergies.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmDemographics.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\gmCrypto.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient\*.pyc"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_patient_demographics.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_gnuMedGP_Toolbar.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_gnumedGP_notebook.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_gnumedGP.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_for_gnumed_browser16_16.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_contacts_toolbar16_16.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_Archive_plugin1.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images_Archive_plugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\images.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\__init__.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmXdtViewer.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmVaccinationsPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmStikoBrowser.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmSQL.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmSnellen.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmShowMedDocs.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmShowLab.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmScanMedDocsNG.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmScanMedDocs.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmRequest.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmPython.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmplNbSchedule.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmOffice.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmNotebookedProgressNoteInputPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmNotebookedPatientEditionPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmMultiSashedProgressNoteInputPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmManual.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmLabJournalPG.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmLabJournal.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmGuidelines.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmEMRTextDumpPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmEMRJournalPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmEMRBrowserPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmDrugDisplay.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmDemographicsEditor.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmContacts.py~"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmContacts.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmConfigRegistry.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmClinicalWindowManager.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\gmAllergiesPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui\*.pyc"
  Delete "$INSTDIR\bin\gnumed.py"
  Delete "$INSTDIR\bitmaps\__init__.py"
  Delete "$INSTDIR\bitmaps\any_body2.png"
  Delete "$INSTDIR\bitmaps\binoculars_form.png"
  Delete "$INSTDIR\bitmaps\bmi_calculator.png"
  Delete "$INSTDIR\bitmaps\default.png"
  Delete "$INSTDIR\bitmaps\empty-face-in-bust.png"
  Delete "$INSTDIR\bitmaps\gnumedlogo.png"
  Delete "$INSTDIR\bitmaps\oneperson.png"
  Delete "$INSTDIR\bitmaps\padlock_closed.png"
  Delete "$INSTDIR\bitmaps\preg_calculator.png"
  Delete "$INSTDIR\bitmaps\save.png"
  Delete "$INSTDIR\bitmaps\serpent.png"
  Delete "$INSTDIR\pixmaps\gnumed.xpm"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmVaccWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmTopPanel.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmTimer.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmTerryGuiParts.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmTalkback.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmSQLSimpleSearch.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmSQLListControl.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmSOAPWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmShadow.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmSelectPerson.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmRichardSpace.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmResizingWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmRegetMixin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmPregWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmPlugin_Patient.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmPlugin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmPhraseWheel.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmPatSearchWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmPatPicWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmPatientHolder.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmMultiSash.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmMultiColumnList.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmMedDocWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmMacro.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmLoginDialog.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmLogin.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmListCtrlMapper.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmLabWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmHorstSpace.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGuiMain.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGuiHelpers.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGP_SocialHistory.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGP_PatientPicture.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGP_Inbox.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGP_HabitsRiskFactors.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGP_FamilyHistorySummary.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmGP_ActiveProblems.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmFormPrinter.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmEMRTextDump.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmEMRStructWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmEMRBrowser.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmEditArea.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmDemographicsWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmDateTimeInput.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmCryptoText.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmCharacterValidator.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmBMIWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmAppoint.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmAllergyWidgets.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gmAbout.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\*.pyc"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\sitecustomize.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\*.pyc"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\__init__.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\__init__.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\transferDBset.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\stripdos.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\show_img.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\set-conf_opt.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\debugging_off.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\CVS\Root"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\CVS\Repository"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools\CVS\Entries"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmWhoAmI.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmSignals.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmSerialTools.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmScriptingListener.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmSchemaRevisionCheck.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmPyCompat.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmPsql.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmPG.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmNull.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmMimeMagic.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmMimeLib.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmMatchProvider.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmLoginInfo.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmLog.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmI18N.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmGuiBroker.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmExceptions.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmDrugView.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmDrugObject.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmDispatcher.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmdbf.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmConfigCommon.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmCLI.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmCfg.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmBusinessDBObject.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmBorg.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\gmBackendListener.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\*.pyc"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\importers\gmLDTimporter.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\importers\*.pyc"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\exporters\__init__.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\exporters\gmPatientExporter.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\exporters\*.pyc"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\__init__.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\README"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmXmlDocDesc.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmXdtObjects.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmXdtMappings.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmVaccination.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmSOAPimporter.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmPerson.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmPathLab.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmOrganization.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmMedDoc.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmKVK.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmForms.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmEMRStructItems.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmDemographicRecord.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmClinNarrative.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmClinItem.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmClinicalRecord.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\gmAllergy.py"
  Delete "${PYTHON_PATH}\Lib\site-packages\Gnumed\business\*.pyc"

  Delete "$SMPROGRAMS\GNUmed\Uninstall.lnk"
  Delete "$SMPROGRAMS\GNUmed\Website.lnk"
  Delete "$SMPROGRAMS\GNUmed\GNUmed.lnk"

  RMDir "$SMPROGRAMS\GNUmed"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\patient"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython\gui"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\wxpython"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon\tools"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\pycommon"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\importers"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\exporters"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed\business"
  RMDir "${PYTHON_PATH}\Lib\site-packages\Gnumed"
  RMDir "$INSTDIR\pixmaps"
  RMDir "$INSTDIR\bin"
  RMDir "$INSTDIR\doc\medical_knowledge\de\STIKO"
  RMDir "$INSTDIR\doc\medical_knowledge\de"
  RMDir "$INSTDIR\doc\medical_knowledge"
  RMDir "$INSTDIR\doc\user-manual"
  RMDir "$INSTDIR\doc"
  RMDir "$INSTDIR\locale\fr_FR\LC_MESSAGES"
  RMDir "$INSTDIR\locale\fr_FR"
  RMDir "$INSTDIR\locale\fr\LC_MESSAGES"
  RMDir "$INSTDIR\locale\fr"
  RMDir "$INSTDIR\locale\es_ES\LC_MESSAGES"
  RMDir "$INSTDIR\locale\es_ES"
  RMDir "$INSTDIR\locale\es\LC_MESSAGES"
  RMDir "$INSTDIR\locale\es"
  RMDir "$INSTDIR\locale\de_DE\LC_MESSAGES"
  RMDir "$INSTDIR\locale\de_DE"
  RMDir "$INSTDIR\locale\de\LC_MESSAGES"
  RMDir "$INSTDIR\locale\de"
  RMDir "$INSTDIR\locale"
  RMDir "$INSTDIR\bitmaps"
  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  SetAutoClose true
SectionEnd