import launch

CI_VERSION = "0.6.1"
needs_install = False

try:
    import clip_interrogator
    if clip_interrogator.__version__ != CI_VERSION:
        needs_install = True
except ImportError:
    needs_install = True

if needs_install:
    launch.run_pip(f"install clip-interrogator-sfw=={CI_VERSION}", "requirements for CLIP Interrogator")