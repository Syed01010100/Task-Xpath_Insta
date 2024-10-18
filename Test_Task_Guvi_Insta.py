from Task_Guvi_Insta import Insta_Guvi
import pytest

web_url = "https://www.instagram.com/guviofficial/"
syed = Insta_Guvi(web_url)


def test_open_url():
    assert syed.open() == True
    print("Page Opened")

def test_count_followers():
    assert syed.Insta_Followers() == True
    print("Follower Counted")

#test the total number of following data
def test_count_following():
    assert syed.Insta_Following() == True
    print("Following Counted")

#close the automation
def test_page_close():
    assert syed.close() == None
    print("Testing Close")

