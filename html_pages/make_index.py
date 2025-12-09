### make an index page (html)

import os
import markdown

### get files in directory
def GetFiles(useDir):

    print("Working in:", useDir)

    # get files in directory
    file_types=[".png",".jpg",".jpeg"]
    file_list=sorted([f for f in os.listdir(useDir) if any([True for x in file_types if x in f.lower()]) ] )
    print("- files found:", len(file_list))
    
    return file_list

### make md page with curated files
def WritePage(file_list, page_name):

    with open(page_name, 'w') as f:
        # title
        f.write(f"# Update Page \n\n")

        # most recent
        f.write(f"## Latest News \n\n")
        f.write(f"[![{file_list[0]}]({file_list[0]})]({file_list[0]}) \n\n")

        # history
        f.write(f"## Old updates \n\n")
        for of in file_list[1::]:
            f.write(f"[![{of}]({of})]({of}) \n\n")

### convert md page to html
def ConvertToHtml(page_name):
    # convert
    with open(page_name, 'r') as m:
        tempMd= m.read()
    # docs on extensions: https://python-markdown.github.io/extensions/
    tempHtml = markdown.markdown(tempMd, extensions=['tables','attr_list'])
    with open(page_name.replace('.md','.html'), 'w') as m:
        m.write(tempHtml)


### List image files in the current directory
if __name__ == "__main__":
    print("\n# running make_index.py\n")

    useDir=os.getcwd()+"/gallery/"
    file_list=GetFiles(useDir)
    page_name="test_page.md"
    WritePage(file_list, page_name)
    ConvertToHtml(page_name)

    print("all done!")




