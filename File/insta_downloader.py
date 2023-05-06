import instaloader
#download all images and videos by instagram username which is public
name = 'username'
instaloader.Instaloader().download_profile(name, profile_pic_only=False)
print('Done')