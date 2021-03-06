#!/bin/sh

rm -rf solutions/
mkdir solutions/
# python3 best_per_cache.py inputs/kittens.in > solutions/kittens.txt
python3 best_per_cache.py inputs/me_at_the_zoo.in > solutions/me_at_the_zoo.txt
echo "me_at_the_zoo done!"
python3 best_per_cache.py inputs/trending_today.in > solutions/trending_today.txt
echo "trending_today done!"
python3 best_per_cache.py inputs/videos_worth_spreading.in > solutions/videos_worth_spreading.txt
echo "videos_worth_spreading done!"

zip solutions/sol.zip parse.py best_per_cache.py tools.py
