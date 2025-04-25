# # Aby dopełnić dotąd zdobytą wiedzę, wyszukaj informacje w zewnętrznych źródłach na temat:
# # Czym jest biblioteka asyncio i jakie zapewnia funkcjonalności?
# # Różnice między korutynami a wątkami
# # Czym jest Future, Task oraz korutyna.
# # Jak działa Event Loop
# # Jak przeprowadzany jest multiprocessing w kontekście asyncio


# Asynchroniczność w Pythonie: asyncio i okolice
# Biblioteka asyncio w Pythonie służy do pisania współbieżnego kodu za pomocą składni async/await. Pozwala na wykonywanie wielu operacji na pozór równocześnie, ale w rzeczywistości działając w jednym wątku. To podejście jest szczególnie przydatne przy operacjach wejścia/wyjścia (I/O), takich jak pobieranie danych z sieci, operacje na plikach czy komunikacja z bazą danych, gdzie czas oczekiwania na odpowiedź jest długi w porównaniu z czasem przetwarzania danych.

# Funkcjonalności asyncio
# Korutyny (coroutines): Funkcje, które mogą być wstrzymywane i wznawiane, co umożliwia "przełączanie się" między zadaniami bez blokowania wątku.
# Pętlę zdarzeń (event loop): Zarządza wykonywaniem korutyn, monitoruje zdarzenia (np. dane dostępne w sieci) i "budzi" odpowiednie korutyny do dalszej pracy.
# Zadania (tasks): Obiekty, które reprezentują wykonywanie korutyny w pętli zdarzeń.
# Przyszłości (futures): Obiekty, które reprezentują wynik operacji, która może jeszcze nie być dostępna.
# Synchronizacja: Narzędzia do synchronizacji korutyn, takie jak блокировки, semafory itp.
# Transporty i protokoły: Abstrakcje do obsługi komunikacji sieciowej.
# Różnice między korutynami a wątkami
# Cecha	Korutyny (asyncio)	Wątki (threading)
# Współbieżność	Współbieżność w jednym wątku (współdzielenie zasobów)	Równoległe wykonywanie w wielu wątkach (potencjalne problemy z zasobami)
# Zarządzanie	Zarządzane przez pętlę zdarzeń	Zarządzane przez system operacyjny
# Przełączanie	Szybkie przełączanie między korutynami (minimalny koszt)	Wolniejsze przełączanie między wątkami (większy koszt)
# Zastosowanie	Operacje I/O (sieć, pliki)	Operacje CPU-bound i I/O-bound
# GIL (CPython)	Omijane przy operacjach I/O	Ogranicza równoległe wykonywanie w CPython


# Asynchroniczność w Pythonie: asyncio i okolice
# Biblioteka asyncio w Pythonie służy do pisania współbieżnego kodu za pomocą składni async/await. Pozwala na wykonywanie wielu operacji na pozór równocześnie, ale w rzeczywistości działając w jednym wątku. To podejście jest szczególnie przydatne przy operacjach wejścia/wyjścia (I/O), takich jak pobieranie danych z sieci, operacje na plikach czy komunikacja z bazą danych, gdzie czas oczekiwania na odpowiedź jest długi w porównaniu z czasem przetwarzania danych.

# Funkcjonalności asyncio
# Korutyny (coroutines): Funkcje, które mogą być wstrzymywane i wznawiane, co umożliwia "przełączanie się" między zadaniami bez blokowania wątku.
# Pętlę zdarzeń (event loop): Zarządza wykonywaniem korutyn, monitoruje zdarzenia (np. dane dostępne w sieci) i "budzi" odpowiednie korutyny do dalszej pracy.
# Zadania (tasks): Obiekty, które reprezentują wykonywanie korutyny w pętli zdarzeń.
# Przyszłości (futures): Obiekty, które reprezentują wynik operacji, która może jeszcze nie być dostępna.
# Synchronizacja: Narzędzia do synchronizacji korutyn, takie jak блокировки, semafory itp.
# Transporty i protokoły: Abstrakcje do obsługi komunikacji sieciowej.
# Różnice między korutynami a wątkami
# Cecha	Korutyny (asyncio)	Wątki (threading)
# Współbieżność	Współbieżność w jednym wątku (współdzielenie zasobów)	Równoległe wykonywanie w wielu wątkach (potencjalne problemy z zasobami)
# Zarządzanie	Zarządzane przez pętlę zdarzeń	Zarządzane przez system operacyjny
# Przełączanie	Szybkie przełączanie między korutynami (minimalny koszt)	Wolniejsze przełączanie między wątkami (większy koszt)
# Zastosowanie	Operacje I/O (sieć, pliki)	Operacje CPU-bound i I/O-bound
# GIL (CPython)	Omijane przy operacjach I/O	Ogranicza równoległe wykonywanie w CPython

# Eksportuj do Arkuszy
# Future, Task i korutyna
# Korutyna: Funkcja, która może być wstrzymana i wznowiona. Oznaczona async i używa await.
# Future: Obiekt reprezentujący wynik, który będzie dostępny w przyszłości.
# Task: Obiekt, który "opakowuje" korutynę i pozwala na jej uruchomienie w pętli zdarzeń. Dziedziczy po Future.
# Jak działa pętla zdarzeń (event loop)
# Pętla zdarzeń nieustannie nasłuchuje na zdarzenia (np. dane przychodzące z sieci, czas, który upłynął).
# Gdy pojawia się zdarzenie, pętla sprawdza, które zadania (taski) są gotowe do działania (np. czekają na te dane).
# Zadania, które mogą działać, są wykonywane (kolejno, w ramach jednego wątku).
# Jeśli zadanie musi poczekać na coś (np. odpowiedź z sieci), jest wstrzymywane, a pętla wraca do nasłuchiwania.
# Proces ten powtarza się, aż wszystkie zadania zostaną wykonane lub pętla zostanie zatrzymana.
# Multiprocessing w kontekście asyncio
# asyncio działa w jednym wątku, więc nie wykorzystuje wielordzeniowości procesora w pełni. Aby skorzystać z wielu rdzeni, można użyć modułu multiprocessing w połączeniu z asyncio. Można na przykład uruchomić kilka pętli zdarzeń w osobnych procesach i komunikować się z nimi za pomocą kolejek.