def jpg_date_group(source, dest, dry = True):
    '''
    Moves or copies JPG files from source dir to dest/date, where
    date is the exif date.
    
    source : str
        Source directory
    dest : str
        Destination directory, under which date subdirectories will be created.
        Should exist.
    dry : bool, default ``True``
        If True, will only do a dry run, not moving any files.
    '''
    files_and_dates = {
        f : Image.open(join(source,f))._getexif()[36867][:10].replace(':','-') 
        for f in os.listdir(source) 
        if (isfile(join(source, f)) and f[-3:].lower() == 'jpg')
    }
    
    
    for f in files_and_dates:
        # create dest/date directory
        new_path = join(dest, files_and_dates[f]) 
        if not os.path.exists(new_path):
            print ('creating', new_path)
            if not dry:
                os.makedirs(new_path)

        # move file
        if not os.path.exists(join(new_path, f)):
            print ('moving ', join(source, f), join(new_path,f))
            if not dry:
                shutil.move(join(source, f), join(new_path,f))
        else: # don't overwrite
            raise ValueError('file already exists', join(new_path, f))
