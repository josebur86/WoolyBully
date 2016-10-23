import os
import predictor
import ui
import sys

ui_port = int(os.environ.get("PORT", 5000))
predictor_port = int(os.environ.get("PORT", 5001))

if len(sys.argv) > 1:
    if sys.argv[1] == "u":
        ui.app.config['TEMPLATES_AUTO_RELOAD'] = True
        ui.app.run(host='0.0.0.0', port=ui_port)
    elif sys.argv[1] == "p":
        predictor.app.run(host='0.0.0.0', port=predictor_port)
else:
    ui.app.config['TEMPLATES_AUTO_RELOAD'] = True
    ui.app.run(host='0.0.0.0', port=ui_port)
