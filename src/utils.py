import re

def remove_substring(text, start, end):
    text_segments = text.split(start)
    text_no_substring = text_segments[0]
    if len(text_segments) > 1:
        for segment in text_segments[1:]:
            if end in segment:
                text_no_substring += '\n' + segment.split(end)[1]
            else:
                print 'ERROR: Did not find "%s" corresponding to "%s".' % (end, start)
                exit()
    return text_no_substring

def remove_comments(text):
    text_no_blk_comments = remove_substring(text, '/*', '*/')
    text_no_comments = remove_substring(text_no_blk_comments, '//', '\n')
    return text_no_comments


def remove_whitespaces(text):
    text_no_whitespaces = ' '.join(text.split())
    return text_no_whitespaces

