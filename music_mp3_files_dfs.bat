pushd C:\Users\Emanuel\Music\musicaa-20230829T045637Z-001\musicaa
   for /r %%a in (*.mp3) do (
      XCOPY /Y "%%a" "C:\Users\Emanuel\Music\mussic"
   )
popd