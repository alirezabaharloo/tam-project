from deep_translator import ChatGptTranslator


def get_persian_date(date_obj):
    """Persian style: 25 اسفند 1402"""
    if hasattr(date_obj, 'created_date'):
        months = {
            1: 'فروردین',
            2: 'اردیبهشت', 
            3: 'خرداد',
            4: 'تیر',
            5: 'مرداد',
            6: 'شهریور',
            7: 'مهر',
            8: 'آبان',
            9: 'آذر',
            10: 'دی',
            11: 'بهمن',
            12: 'اسفند'
        }
        day = date_obj.created_date.day
        month = months[date_obj.created_date.month]
        year = date_obj.created_date.year
        return f"{day} {month} {year}"
    return None


def filter_vocabulary(text: str, length: int) -> str:
    """Filter the vocabulary of the text to the length"""
    filterd_text = text.split(' ')
    return ' '.join(filterd_text[:length]) + '...' if len(filterd_text) > length else text

    