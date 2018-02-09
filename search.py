# -*- coding: UTF-8 -*-
import os, time, fnmatch, csv
class search:
  def __init__(self, path, search_string, file_filter):
    self.search_path = path
    self.search_string = search_string
    self.file_filter = file_filter
    print("Search '%s' in [%s]..." % (
      self.search_string, self.search_path
    ))
    print("_" * 80)
    time_begin = time.time()
    file_count = self.walk()
    print("_" * 80)
    print("%s files searched in %0.2fsec." % (
      file_count, (time.time() - time_begin)
    ))

  #遍历文件
  def walk(self):
    file_count = 0
    for root, dirlist, filelist in os.walk(self.search_path, followlinks=True):
      for filename in filelist:
        for file_filter in self.file_filter:
          if fnmatch.fnmatch(filename, file_filter):
            self.search_file(os.path.join(root, filename))
            file_count += 1
    return file_count

  #读写文件
  def search_file(self, filepath):
    try:
      f = open(filepath, "r", encoding='UTF-8')
      content = f.read()
      f.close()
      if self.search_string in content:
        self.cutout_content(content, filepath)
    except :
      pass

  #打印出重复内容，保存至CSV
  def cutout_content(self, content, filepath):
    current_pos = 0
    search_string_len = len(self.search_string)
    for i in range(max_cutouts):
      try:
        pos = content.index(self.search_string, current_pos)
      except ValueError:
        break
      content_window = content[ pos - content_extract : pos + content_extract ]
      print(">>>", content_window)
      print("filepath", filepath)

      with open('search.csv', 'a+', newline='', encoding='gb18030') as csvfile:
        spamwriter = csv.writer(csvfile)
        data = ([str(self.search_string), str(content_window), str(filepath)])
        spamwriter.writerow(data)

      current_pos += pos + search_string_len

if __name__ == "__main__":
  search_path = r"c:\"
  file_filter = ("*.php","*.java ","*.html","*.txt","*.json")
  content_extract = 20
  max_cutouts = 50

  with open("ad.csv", "r", encoding="gbk") as csvfile:
    # 读取csv文件，返回的是迭代类型
    read = csv.reader(csvfile)
    for i in read:
      print(i[0])
      search_string = i[0]
      search(search_path, search_string, file_filter)


