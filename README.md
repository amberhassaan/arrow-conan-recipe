Let the root of this repository be $curr_dir

Build libarrow to your conan profile by:

```
conan create $curr_dir/build_recipe.py --build=missing
```

Configure the build repository of katana (or any other repo that depends on
libarrow):

```
PYTHONPATH=$PYTHONPATH:<path-to-katana-enterprise/config> conan install -if .  --build=missing  $curr_dir/config.py
```
