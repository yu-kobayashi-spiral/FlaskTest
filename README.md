# 環境設定

・pyenvとflaskをインストール

・pythonのバージョンは3.9.5（pyenvでインストールしてバージョン切り替える）

・.zshrcと.zprofile作成してそれぞれパスを通す

.zprofile
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

.zshrc
eval "$(pyenv init -)"
