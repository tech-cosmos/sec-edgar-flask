import unittest
import shutil
import os

class TestLocalStorage(unittest.TestCase):
  def setUp(self):
        
    self.dest_path = "/media/shivam/backup/data/sec/submissions"

  def test_delete_folder(self):
        
    # check if the folder exists
    if os.path.exists(self.dest_path) and os.path.isdir(self.dest_path):
        
        self.assertTrue(os.path.exists(self.dest_path))
        
        # delete the folder and its contents
        shutil.rmtree(self.dest_path)

        # check that the folder no longer exists
        self.assertFalse(os.path.exists(self.dest_path))

    else:
        print('Folder does not exist')
        
        
if __name__ == '__main__':
  unittest.main()
