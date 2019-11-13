CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt

solution: P11.cpp
	 $(CXX) $(CXXFLAGS) P11.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

