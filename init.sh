#!/bin/bash
set -euo pipefail

cd /workspace
git clone https://${GITHUB_TOKEN}@github.com/ShrykeZ/LWC.git /workspace/myproject

chmod +x /workspace/myproject/startup.sh
sed -i 's/\r$//' /workspace/myproject/startup.sh
bash /workspace/myproject/startup.sh
