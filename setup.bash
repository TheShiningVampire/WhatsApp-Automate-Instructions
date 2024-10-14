# Basic Setup
pkg install git
pkg install python
termux-setup-storage
apt upgrade openssl
apt install golang
pkg install ranger

# Make Directory
mkdir -p .termux/tasker/ && cd .termux/tasker/

# Clone the whatsmeow repo
git clone https://github.com/TheShiningVampire/whatsmeow

cd whatsmeow/sender

go mod tidy

go build -o sender

# Copy sender to /data/data/com.termux/files/home/.termux/tasker/
cp sender /data/data/com.termux/files/home/.termux/tasker/

cd /data/data/com.termux/files/home/.termux/tasker/


