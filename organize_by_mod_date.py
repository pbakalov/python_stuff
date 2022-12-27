import os 
from os.path import isfile, join
import shutil

def group_by_mod_time(source, dest, move=True, dry = True):
    '''
    Moves or copies files from source dir to dest/date, where
    date is the modified date.
    
    source : str
        Source directory
    dest : str
        Destination directory, under which date subdirectories will be created.
        Should exist.
    move : bool, default ``True``
        If ``True`` will move the files to ``dest``, if ``False`` will keep the originals and 
        create copies in dest.
    dry : bool, default ``True``
        If True, will only do a dry run, not moving any files.
    '''
    files_and_dates = {
#         f : Image.open(join(source,f))._getexif()[36867][:10].replace(':','-') 
        f : parser.parse(
            time.ctime(os.path.getmtime(os.path.join(source, f)))
        ).strftime('%Y-%m-%d')
        for f in os.listdir(source) 
        if (isfile(join(source, f)))# and f[-3:].lower() == 'jpg')
    }

    print ("unique dates:", len(set(files_and_dates.values())))
    
    
    for f in files_and_dates:
        # create dest/date directory
        new_path = join(dest, files_and_dates[f]) 
        if not os.path.exists(new_path):
            print ('creating', new_path)
            if not dry:
                os.makedirs(new_path)

        # move file
        if not os.path.exists(join(new_path, f)):
                if move:
                    print ('moving ', join(source, f), join(new_path,f))
                    if not dry:
                        shutil.move(join(source, f), join(new_path,f))
                else:
                    print ('copying ', join(source, f), join(new_path,f))
                    if not dry:
                        shutil.copy(join(source, f), join(new_path,f))

        else: # don't overwrite
            raise ValueError('file already exists', join(new_path, f))

