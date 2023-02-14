from tech_news.analyzer.reading_plan import ReadingPlanService
from unittest.mock import patch
import pytest


def mock_list():
    mock1 = {
        "_id": {"$oid": "63ea68e9ee4750d72db4df0e"},
        "url": "https://blog.betrybe.com/tecnologia/exemplos-de-algoritmos/",
        "title": "computação",
        "timestamp": "03/02/2023",
        "writer": "Lucas Custódio",
        "reading_time": 5,
        "summary": "Quando falamos de algoritmos, pensamos em matemática.",
        "category": "Tecnologia",
    }
    mock2 = {
        "_id": {"$oid": "63ea68e9ee4750d72db4df0f"},
        "url": "https://blog.betrybe.com/carreira/trybetalks-gaules/",
        "title": "TrybeTalks — Gaules",
        "timestamp": "30/01/2023",
        "writer": "Lucas Custódio",
        "reading_time": 9,
        "summary": "Gaules divide um pouco de sua experiência na Trybe.",
        "category": "Carreira",
    }
    mock3 = {
        "_id": {"$oid": "63ea68e9ee4750d72db4df10"},
        "url": "https://blog.betrybe.com/tecnologia/next-js/",
        "title": "Next JS: o que é, para que serve e por que usar?",
        "timestamp": "27/01/2023",
        "writer": "Lucas Marchiori",
        "reading_time": 13,
        "summary": "Conhecer as principais tecnologias do mercado.",
        "category": "Tecnologia",
    }
    return [mock1, mock2, mock3]


def test_reading_plan_group_news():
    mock_assert = {
        "readable": [
            {
                "unfilled_time": 5,
                "chosen_news": [("computação", 5)],
            },
            {
                "unfilled_time": 1,
                "chosen_news": [("TrybeTalks — Gaules", 9)],
            },
        ],
        "unreadable": [
            ("Next JS: o que é, para que serve e por que usar?", 13),
        ],
    }

    with patch("tech_news.analyzer.reading_plan.find_news", mock_list):
        print(ReadingPlanService.group_news_for_available_time(10))
        assert (
            ReadingPlanService.group_news_for_available_time(10) == mock_assert
        )
        assert ReadingPlanService.group_news_for_available_time(10)[
            "unreadable"
        ] == [("Next JS: o que é, para que serve e por que usar?", 13)]
        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(0)
