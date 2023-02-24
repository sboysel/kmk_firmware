# sboysel KMK keymaps

Some notes on keeping my own keymaps on a fork of `KMKfw/kmk_firmware`

- `upstream` is `KMKfw/kmk_firmware`
- `origin` is `KMKfw_firmware`

```
git clone git@github.com:sboysel/kmk_firmware.github
cd kmk_firmware
git remote add upstrea git@github.com:KMKfw/kmk_firmware.git
git pull upstream master
git push origin master
```

Leave `master` alone. Commit changes to `sboysel`, pull `master` and rebase,
push `sboysel` to `origin`.

```
git checkout -b sboysel
# modifications ...
git add user_keymaps/sboysel 
git commit -m "changes to my keymaps"
git pull upstream master
git push origin master
git rebase master
git push -u origin sboysel
```

# updating firmware/keymaps

Install KMK

```
cd kmk_firmware
git checkout sboysel
cp -avr kmk /run/media/sam/CIRCUITPY
cp boot.py /run/media/sam/CIRCUITPY
```

Copy board definition

```
cp boards/crowboard/kb.py /run/media/sam/CIRCUITPY/kb.py
```

Copy keymap

```
cp user_keymaps/sboysel/36.py /run/media/sam/CIRCUITPY/code.py
```

Edit keymap as needed

```
nvim /run/media/sam/CIRCUITPY/code.py
```

# keymaps

- `36.py`: a stripped down version of Miryoku tailored to my needs. Can be 
  adapted to a 4x10 grid.
