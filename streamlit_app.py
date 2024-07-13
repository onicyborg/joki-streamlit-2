import streamlit as st

# Adding name and NIM at the top
st.sidebar.title("Informasi Pembuat")
st.sidebar.write("Dibuat oleh: Nasywa Meriq Aulia Putri")
st.sidebar.write("NIM: 152310069")

def is_prime(n):
    """Function to check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    """Function to find prime numbers in a given range"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Title and description
st.title("🚀 Pencari Bilangan Prima")
st.write("Temukan bilangan prima dalam rentang yang Anda tentukan!")

# Input from the user
start_num = st.number_input("Masukkan Angka Awal:", value=1, step=1)
end_num = st.number_input("Masukkan Angka Akhir:", value=100, step=1)

# Button to submit the range
if st.button("Cari Bilangan Prima"):
    if start_num > end_num:
        st.error("Angka awal harus lebih kecil dari angka akhir. Silakan coba lagi!")
    else:
        prime_numbers = find_primes(start_num, end_num)
        if prime_numbers:
            st.success(f"Bilangan Prima antara {start_num} dan {end_num} adalah:")
            st.write(", ".join(map(str, prime_numbers)))
            st.balloons()
        else:
            st.warning(f"Tidak ada bilangan prima yang ditemukan antara {start_num} dan {end_num}.")
