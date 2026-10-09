from pathlib import Path
import subprocess,os,time,sys
project,suite,log=sys.argv[1:4]
path=Path(log);env=os.environ.copy();env['SDL_AUDIODRIVER']='dummy'
args=[sys.argv[4] if len(sys.argv)>4 else '/home/seguel/Juegos/renpy/renpy.sh',project,'test',suite,'--report-detailed','--overwrite-screenshots']
with path.open('w') as out:
 p=subprocess.Popen(args,stdout=out,stderr=subprocess.STDOUT,env=env)
 try:
  deadline=time.monotonic()+1200
  while time.monotonic()<deadline:
   content=path.read_text(errors='replace')
   if '[rpytest] Status: PASSED' in content or '[rpytest] Status: FAILED' in content:
    passed='[rpytest] Status: PASSED' in content
    p.terminate()
    try:p.wait(timeout=3)
    except subprocess.TimeoutExpired:p.kill();p.wait()
    print('Prueba finalizada; ventana cerrada automáticamente. Resultado:', 'PASSED' if passed else 'FAILED')
    sys.exit(0 if passed else 1)
   if p.poll() is not None:
    print('El motor terminó antes del resumen. Código:',p.returncode);sys.exit(p.returncode or 1)
   time.sleep(1)
  print('Tiempo de prueba agotado.');sys.exit(2)
 finally:
  if p.poll() is None:p.kill();p.wait()
